import { BaseEntity } from "src/common/entities/base.entity";
import { ArtistEntity } from "./artist.entity";
import {Column, Entity, ManyToMany, ManyToOne} from "typeorm";

@Entity()
export class MovieEntity extends BaseEntity{
    @Column()
    title: string;

    @Column()
    descripition: string;

    @Column()
    duration: number;

    @Column()
    year: number;

    @Column()
    image: string;

    @ManyToMany(() => ArtistEntity, (artist) => artist.moviesCast)
    cast: ArtistEntity[];
    
    @ManyToOne(() => ArtistEntity, (artist) => artist.moviesDirected)
    director: ArtistEntity[];
}